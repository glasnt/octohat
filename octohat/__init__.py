#!/usr/bin/env python

import argparse
import sys
from .helpers import * 

def main(): 

  parser = argparse.ArgumentParser()
  parser.add_argument("repo_name", help="githubuser/repo")
  parser.add_argument("-g", "--generate-html", action='store_true', help="Generate output as HTML")
  parser.add_argument("-l", "--limit", help="Limit to the last x Issues/Pull Requests", type=int, default=0)
  args = parser.parse_args()  

  repo_name = args.repo_name

  if not repo_exists(repo_name): 
    print("Repo does not exist: %s" % repo_name)
    sys.exit(1)

  code_contributors = get_code_contributors(repo_name)
  code_commentors = get_code_commentors(repo_name, args.limit)

  non_code_contributors = []
  for user in code_commentors:
    user_name, avatar = user 
    if user_name not in code_contributors:
      non_code_contributors.append({'user_name': user_name, 'avatar': avatar})

  print("Code contributions: %d" % len(code_contributors))
  print("Non-code contributions: %d" % len(non_code_contributors))

  if args.generate_html:
    html_file = "%s_contrib.html" % repo_name.replace("/", "_")
    f = open(html_file, "w")

    title = "Non-code contributions for %s" % repo_name
    f.write("<title>%s</title>\n" %  title)
    f.write("<h1>%s</h1>\n" % title)
    if args.limit > 0:
      f.write("(for the most recent %d issues/pull requests)" % args.limit)
    for user in non_code_contributors: 
      url = "https://github.com/%s/issues?q=involves:%s" % (repo_name, user["user_name"])
      f.write("<a href='%s'><img src='%s' width='128'></a>\n" % (url, user["avatar"]))
    f.write("<br><br>Generated by <a href='https://github.com/glasnt/octohat'>octohat</a>")

    print("Generated HTML representation, saved to %s" % html_file)
  else: 
    for user in non_code_contributors: 
      print(user["user_name"])

if __name__ == "__main__":
    main()
