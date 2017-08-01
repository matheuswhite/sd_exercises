from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 8000

#This class will handles any incoming request from
#the browser 
class Server(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		root_dir = '.'

		try:
			if self.path.endswith('.json'):
				f = open(root_dir + self.path) #open requested file

				#send code 200 response
				self.send_response(200)

				#send header first
				self.send_header('Content-type','text-html')
				self.end_headers()

				#send file content to client
				self.wfile.write(f.read())
				f.close()
				return
			elif self.path.endswith('.html'):
				f = open(root_dir + self.path) #open requested file

				#send code 200 response
				self.send_response(200)

				#send header first
				self.send_header('Content-type','text-html')
				self.end_headers()

				#send file content to client
				self.wfile.write(f.read())
				f.close()
				return

		except IOError:
			self.send_error(404, 'file not found')

	def do_POST(self):
		root_dir = '.'

		try:
			if self.path.endswith('.json'):
				f = open(root_dir + self.path) #open requested file

				#send code 200 response
				self.send_response(200)

				#send header first
				self.send_header('Content-type','text-html')
				self.end_headers()

				content_length = int(self.headers['Content-Length'])
				file_content = self.rfile.read(content_length)

		        # Do what you wish with file_content
		        print file_content

				#send file content to client
				self.wfile.write("Content updated!")
				f.close()
				return

		except IOError:
			self.send_error(404, 'file not found')

	def do_PUT(self):
		root_dir = '.'

		try:
			f = open(root_dir + self.path, "r+") #open requested file
			f.seek(0)
			f.write(self.rfile.read())
			f.truncate()
			f.close()

		except IOError:
			f = open(root_dir + self.path, "w")
			f.write('''write something''')
			f.close()

		#send code 200 response
		self.send_response(200)

		#send header first
		self.send_header('Content-type','text-html')
		self.end_headers()

		self.wfile.write("File created with success")

	def do_DELETE(self):
		root_dir = '.'

		try:
			if self.path.endswith('.json'):
				f = open(root_dir + self.path) #open requested file

				#send code 200 response
				self.send_response(200)

				#send header first
				self.send_header('Content-type','text-html')
				self.end_headers()

				#send file content to client
				self.wfile.write(f.read())
				f.close()
				return
			elif self.path.endswith('.html'):
				f = open(root_dir + self.path) #open requested file

				#send code 200 response
				self.send_response(200)

				#send header first
				self.send_header('Content-type','text-html')
				self.end_headers()

				#send file content to client
				self.wfile.write(f.read())
				f.close()
				return

		except IOError:
			self.send_error(404, 'file not found')

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('localhost', PORT_NUMBER), Server)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()