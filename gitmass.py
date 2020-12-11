#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import git
import os
import adapters
from helpers.ArgsHelper import ArgsHelper
from helpers.DetectVcs import DetectVcs
from adapters.AdapterInterface import AdapterInterface


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-url', type=str, nargs=None, help='url of vcs, ex: `https://vcs.yourdomain.com`')
    parser.add_argument('--org', '-o', type=str, nargs=None, help='namespace or organization name')
    parser.add_argument('--user', '-u', type=str, nargs=None, default="0", help='user name')
    parser.add_argument('--token', '-t', type=str, nargs=None, help='private token')
    parser.add_argument('--dir', '-d', type=str, nargs=None, help='local directory for repos')
    args = parser.parse_args()
    args.url = ArgsHelper().check_arg(args.url, "url")
    args.org = ArgsHelper().check_arg(args.org, "organization")
    args.dir = ArgsHelper().check_arg(args.dir, "directory", ".")
    args.token = ArgsHelper().check_arg(args.token, "token", is_password=True)
    args.user = ArgsHelper().check_arg(args.user, "username", "0")

    vcs_type = detect_vcs(args.url)
    """ username for Bitbucket is mandatory. We check it again """
    if vcs_type == "Bitbucket" and args.user == "0":
        args.user = ArgsHelper().check_arg(args.user, "username")

    params = {"token": args.token, "org": args.org, "user": args.user, "url": args.url}
    adapter_class = eval('adapters.' + vcs_type['adapter'] + 'Adapter')(params)

    obj = AdapterInterface(adapter_class, m=adapter_class.get_repos)
    result = obj.m()
    if not result["success"]:
        print(result["message"])
        exit(1)

    for repo in result["results"]:
        dir_name = args.dir + "/" + repo["name"]
        if os.path.exists(dir_name):
            print("Pulling %s" % repo['name'])
            git.Repo(dir_name).remotes.origin.pull()
        else:
            print("Cloning %s" % repo['name'])
            git.Repo.clone_from(repo["url"], dir_name)
    print("All done!")


def detect_vcs(url):
    vcs = DetectVcs(url).detect()
    return vcs


if __name__ == "__main__":
    main()
