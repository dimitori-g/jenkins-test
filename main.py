import os, sys, subprocess

tests_dir = "tests"

if len(sys.argv) > 1:
  print(sys.argv[1])
  file = os.path.join(tests_dir, sys.argv[1])
  if not os.path.isfile(file):
    sys.exit("File not exists")
  subprocess.run(["python3", file])
else:
  files = os.listdir(tests_dir)
  for file in sorted(files):
    print(file)
    subprocess.run(["python3", os.path.join(tests_dir, file)])

