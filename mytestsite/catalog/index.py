#!python
print("Content-Type: text/html")
print()
import cgi, os
form = cgi.FieldStorage()

fileList = os.listdir('data/')
listStr = ''
for fileName in fileList:
	listStr += '<li><a href="index.py?id={filename}">{filename}</a></li>'.format(filename = fileName)

if 'id' in form:
	pageId = form["id"].value
	fileDocs = open('data/{pageId}'.format(pageId = pageId), "r").read()
	link='<a href="update.py?id={}">Update</a>'.format(pageId)
	delete_Link = """
		<form action="process_delete.py" method="post">
			<input type="hidden" name="pageId" value="{}">
			<input type="submit" value="Delete">
		</form>
	""".format(pageId)
else:
	pageId = "WEB"
	fileDocs = "WEB is good"
	link='<a href="create.py">Create</a>'
	delete_Link = ""

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  {Link}
  {delete_Link}
  <h2>{title}</h2>
  <p>{fileDocs}
  </p>
</body>
</html>
'''.format(title=pageId, fileDocs=fileDocs, listStr=listStr, Link=link, delete_Link=delete_Link))
