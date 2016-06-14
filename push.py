# coding:utf-8
import os
import sys
def main(commit_message):
    os.system('git add -A')
    os.system('git commit -m ' + commit_message)
    os.system('git fetch origin')
    os.system('git rebase origin/master')
    os.system('git push origin master')

if __name__ == '__main__':
	print len(sys.argv)
	if len(sys.argv) < 2:
		print "usage: python push commit_message"
	else:
		commit_message = sys.argv[1]
    	main(commit_message)