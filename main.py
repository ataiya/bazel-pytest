"""A simple example Bazel test."""
import argparse

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--foo", type=int, default="123")
parser.add_argument("--dryrun", action='store_true')
FLAGS = parser.parse_args()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

foo = FLAGS.foo
# ... do something with foo

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

if FLAGS.dryrun:
  print("executing dryrun")
  assert False

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

if __name__ == "__main__":
  print("executing main: ", foo)
