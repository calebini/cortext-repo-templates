"""Compile generated output with native Go tooling when installed (required in Go CI)."""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('go_scaffold', ROOT / 'scripts/scaffold.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@unittest.skipUnless(shutil.which('go'), 'Go is not installed; Go smoke CI supplies it')
class GoProfileTests(unittest.TestCase):
    def test_native_initialization_and_quality_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'sample'
            MODULE.scaffold('go', 'sample-app', target)
            env = dict(os.environ, GOTOOLCHAIN='local', CGO_ENABLED='1')

            def run(*args):
                result = subprocess.run(args, cwd=target, env=env, capture_output=True,
                                        encoding='utf-8', timeout=120)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout

            run('go', 'mod', 'init', 'example.com/sample-app')
            run('go', 'mod', 'tidy')
            self.assertEqual(run('gofmt', '-l', '.'), '')
            # Prove the race command exercises actual concurrent code; this fixture
            # belongs to template verification, not the generated greeting starter.
            (target / 'main_test.go').write_text(
                'package main\n\nimport "testing"\n\n'
                'func TestOwnedGoroutine(t *testing.T) {\n'
                '\tdone := make(chan int)\n'
                '\tgo func() { done <- 42 }()\n'
                '\tif got := <-done; got != 42 { t.Fatalf("got %d", got) }\n'
                '}\n')
            run('gofmt', '-w', 'main_test.go')
            for args in [('mod', 'tidy', '-diff'), ('vet', './...'), ('test', './...'),
                         ('test', '-race', './...'), ('build', './...')]:
                run('go', *args)
            run('go', 'build', '-trimpath', '-o', 'bin/sample-app', '.')
            self.assertEqual(run('go', 'run', '.'), 'sample-app\n')
            self.assertFalse((target / 'go.sum').exists())


if __name__ == '__main__':
    unittest.main()
