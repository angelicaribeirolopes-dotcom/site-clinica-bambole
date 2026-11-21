# Gera o site em dist/. Edite build_head.py, build_pages.py, build_articles.py, build_tail.py e content.py.
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT); sys.path.insert(0, ROOT)
src = "\n".join(open(f, encoding="utf-8").read() for f in ["build_head.py", "build_pages.py", "build_articles.py", "build_tail.py"])
exec(compile(src, "build", "exec"))
