#!/usr/bin/env python3
import os, sys, fnmatch, re
import time
import requests

startTime = time.time()

__version__ = 1.0

def check_basic_style(filepath):
	fixedErrors = 0

	with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
		content = file.readlines()
		lineNum = 0
		openBraces = [0, 0]
		newContent = ""
		fixedErrors = 0
		for line in content:
			#print(line)
			#input("Press Enter to continue...")
			lineNum +=1
			equalSign = 0
			if not line.startswith("#"): #If the line doesn't start with a comment
				if "{" in line: #if there is an open brace in this line
					hasComment = re.search(r'#.*[{}]+', line, re.M | re.I)  # If comment at the start or before {
					if not hasComment:  #if the line doesn't have a comment before the open brace
						openBraces[0] += line.count('{')
						#count total open braces and subtract open braces that are easy to find and used correctly
						closingBraces = line.count('{') - line.count(' {\n') - line.count(' { ')

						#if there are braces we couldn't find using efficient .count, use powerful inefficient regex
						if closingBraces > 0:
							noSpaceleftOfBracket = re.search(r'(.*[^\s]+){(.*?\s?)', line,
															 re.M | re.I)  # If no space before or after brace

							# noSpacerightOfBracket = re.search(r'}([^\s]+(.*))(\n?)', line,re.M | re.I)   # If no space before or after brace

							if noSpaceleftOfBracket:
								#print(line)
								#print(noSpaceleftOfBracket.group(1))
								line = re.sub(r'(.*[^\s]+){(.*?\s?)', r"\1 {\2", line)
								#print(line)
								#input()
								fixedErrors += 1

							noSpacerightOfBracket = re.search(r'(.*){([^\s]+?)', line,re.M | re.I)  # If no space before or after brace
							if noSpacerightOfBracket:
								#print(line)
								#print(noSpacerightOfBracket.group(1))
								line = re.sub(r'(.*){([^\s]+?)', r"\1{ \2", line)
								#line = re.sub(r'}((?!\n).)*([^\s]+(.*))(\n?)', r"} \1\2", line)
								#print(line)
								#print(line)
								#input()
								fixedErrors += 1

				if "}" in line: #if there is an close brace in this line
					hasComment = re.search(r'#.*[{}]+', line, re.M | re.I)  # If comment at the start or before {
					if not hasComment: #if the line doesn't have a comment before the open brace
						openBraces[0] += -line.count('}')
						#count total close braces and subtract open braces that are easy to find and used correctly
						openingingBraces = line.count('}') - line.count(' }\n') - line.count(' } ')

						#if there are braces we couldn't find using efficient .count, use powerful inefficient regex
						if openingingBraces > 0:

							noSpaceleftOfBracket = re.search(r'(.*[^\s]+)}(.*?\n?)', line,re.M | re.I)   # If no space before or after brace
							if noSpaceleftOfBracket:
								#print(line)
								#print(noSpaceleftOfBracket.group(1))
								line = re.sub(r'(.*[^\s]+)}(\s?)', r"\1 }\2", line)
								#print(line)
								#input()
								fixedErrors += 1

							noSpacerightOfBracket = re.search(r'(.*)}([^\s]+?)', line, re.M | re.I)  # If no space before or after brace
							if noSpacerightOfBracket:
								#print(line)
								#print(noSpacerightOfBracket.group(1))
								line = re.sub(r'(.*)}([^\s]+?)', r"\1} \2", line)
								#line = re.sub(r'}((?!\n).)*([^\s]+(.*))(\n?)', r"} \1\2", line)
								#print(line)
								#input()
								fixedErrors += 1

							#hasNoSpace = re.search(r'([^\s]+)}|}([^\s]+)', line,re.M | re.I)   # If no space before or after brace
							#if hasNoSpace: #If regex finds open braces not styled correctly
								#print("ERROR: Missing an space before or after close brace at {0} Line number: {1}".format(filepath, lineNum))
								#input("Press Enter to continue...")
								#fixedErrors += 1

				if "=" in line: #if the line has an equal sign
					equalSign = line.count('=') - line.count(' = ') + line.count('  =') + line.count('=  ')
					if "  =" in line:
						#print(line)
						line = re.sub(r'  =', r" =", line)
						#print(line)
						#input()
						equalSign = equalSign - line.count('  =')
						fixedErrors += 1
					if "=  " in line:
						#print(line)
						line = re.sub(r'=  ', r"= ", line)
						#print(line)
						#input()
						equalSign = equalSign - line.count('=  ')
						fixedErrors += 1
					if equalSign != 0:
						noSpaceLeftofEqualSign = re.search(r'(.*[^\s]+)=(.*)?', line, re.M | re.I)  # If no space before or after brace
						if noSpaceLeftofEqualSign:
							line = re.sub(r'(.*[^\s]+)=(.*)?', r"\1 =\2", line)
							fixedErrors += 1

						noSpaceRightofEqualSign = re.search(r'(.*)=([^\s]+.*)', line, re.M | re.I)  # If no space before or after brace
						if noSpaceRightofEqualSign:
							line = re.sub(r'(.*)=([^\s]+.*)?', r"\1= \2", line)
							fixedErrors += 1



				if "	" in line: #if 4 spaces in the line
					line = re.sub(r'	', r"\t", line)
					#print("ERROR: spaces indent (4) detected instead of tab at {0} Line number: {1}".format(filepath,lineNum))
					fixedErrors += 1
			newContent +=line
	file.close()

	if fixedErrors != 0:
		with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
			file.write(newContent)
			#print("Fixed: ", filepath,)
		file.close()

	return fixedErrors


def main():
	print("Validating Basic Style - Secondary Check")

	files_list = []
	bad_count = 0
	message = ""

	# Allow running from root directory as well as from inside the tools directory
	scriptDir = os.path.realpath(__file__)
	rootDir = os.path.dirname(os.path.dirname(scriptDir))

	for root, dirnames, filenames in os.walk(rootDir + '/'+ 'common' + '/'):
		for filename in fnmatch.filter(filenames, '*.txt'):
			files_list.append(os.path.join(root, filename))

	for root, dirnames, filenames in os.walk(rootDir + '/'+ 'events' + '/'):
		for filename in fnmatch.filter(filenames, '*.txt'):
			files_list.append(os.path.join(root, filename))

	for root, dirnames, filenames in os.walk(rootDir + '/'+ 'history' + '/'):
		for filename in fnmatch.filter(filenames, '*.txt'):
			files_list.append(os.path.join(root, filename))

	for filename in files_list:
		bad_count = bad_count + check_basic_style(filename)

	print("Fixed " + str(bad_count) + " styling mistakes")
	message += "Fixed " + str(bad_count) + " styling mistakes\n"

	if bad_count == 0:
		print ("No stylization to fix. Do not post.")
		exit

	try:
		# GitHub API setup
		repo = os.environ['GITHUB_REPOSITORY']
		token = sys.argv[1]
		headers = {
			'Authorization': f'token {token}',
			'Accept': 'application/vnd.github.v3+json'
		}
		payload = {'body': message}

		if "GITHUB_EVENT_NAME" in os.environ and os.environ['GITHUB_EVENT_NAME'] == 'pull_request':
			# For pull requests
			pr_number = os.environ['GITHUB_REF'].split('/')[2]
			url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
			r = requests.post(url, json=payload, headers=headers)
			print("Posted results to pull request")
		else:
			# For direct commits
			commit_sha = os.environ['GITHUB_SHA']
			url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}/comments"
			r = requests.post(url, json=payload, headers=headers)
			print("Posted results to commit")
	except Exception as e:
		print(f"Couldn't post results to GitHub: {str(e)}")


	print ('The script took {0} second!'.format(time.time() - startTime))

if __name__ == "__main__":
	sys.exit(main())
