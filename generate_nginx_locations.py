import os

status_codes = {
  100: "100 Continue",
	101: "101 Switching Protocols",
	102: "102 Processing",
	103: "103 Early Hints",
	200: "200 OK",
	201: "201 Created",
	202: "202 Accepted",
	203: "203 Non-Authoritative Information",
	204: "204 No Content",
	205: "205 Reset Content",
	206: "206 Partial Content",
	207: "207 Multi-Status",
	208: "208 Already Reported",
	226: "226 IM Used",
	300: "300 Multiple Choices",
#	301: "301 Moved Permanently",
#	302: "302 Found (Moved Temporarily)",
#	303: "303 See Other",
	304: "304 Not Modified",
	305: "305 Use Proxy",
	306: "306 (reserved)",
#	307: "307 Temporary Redirect",
#	308: "308 Permanent Redirect",
	400: "400 Bad Request",
	401: "401 Unauthorized",
	402: "402 Payment Required",
	403: "403 Forbidden",
	404: "404 Not Found",
	405: "405 Method Not Allowed",
	406: "406 Not Acceptable",
	407: "407 Proxy Authentication Required",
	408: "408 Request Timeout",
	409: "409 Conflict",
	410: "410 Gone",
	411: "411 Length Required",
	412: "412 Precondition Failed",
	413: "413 Payload Too Large",
	414: "414 URI Too Long[16]",
	415: "415 Unsupported Media Type",
	416: "416 Range Not Satisfiable",
	417: "417 Expectation Failed",
	421: "421 Misdirected Request",
	422: "422 Unprocessable Entity",
	423: "423 Locked",
	424: "424 Failed Dependency",
	425: "425 Too Early",
	426: "426 Upgrade Required",
	428: "428 Precondition Required",
	429: "429 Too Many Requests",
	431: "431 Request Header Fields Too Large",
	451: "451 Unavailable For Legal Reasons",
	418: "418 I'm a teapot",
	420: "420 Policy Not Fulfilled",
	444: "444 No Response",
	449: "449 The request should be retried after doing the appropriate action",
	499: "499 Client Closed Request",
	500: "500 Internal Server Error",
	501: "501 Not Implemented",
	502: "502 Bad Gateway",
	503: "503 Service Unavailable",
	504: "504 Gateway Timeout",
	505: "505 HTTP Version not supported",
	506: "506 Variant Also Negotiates",
	507: "507 Insufficient Storage",
	508: "508 Loop Detected",
	509: "509 Bandwidth Limit Exceeded",
	510: "510 Not Extended",
	511: "511 Network Authentication Required"
}
redirect_status_codes = [301, 302, 303, 307, 308]
html_return = "\t\tlocation = /?1 {\n\t\t\treturn ?1 \"<html>\\n<head><title>?2</title></head>\\n<body>\\n<center><h1>?2</h1></center>\\n<hr><center>nginx/$nginx_version</center>\\n</body>\\n</html>\";\n\t\t}\n"
redirect_return = "\t\tlocation = /?1 {\n\t\t\treturn ?1 $scheme://$http_host/;\n\t\t}\n"

script_dir = os.path.dirname(__file__)
rel_path = "conf/nginx.conf"
abs_path = os.path.join(script_dir, rel_path)

with open(abs_path, "r+") as f:
  # list to store new lines
  lines = []
  # copy old lines until start label
  for line in f:
    lines.append(line)
    if "#start_location_config_label" in line:
      break
  # construct new location config lines
  for i in range(1000):
    if i in redirect_status_codes: lines.append(redirect_return.replace("?1", str(i).zfill(3)))
    elif  i in status_codes: lines.append(html_return.replace("?1", str(i).zfill(3)).replace("?2", status_codes[i]))
    else: lines.append(html_return.replace("?1", str(i).zfill(3)).replace("?2", str(i).zfill(3)))
  # delete / skip old location config lines until end label
  for line in f:
    if "#end_location_config_label" in line:
      lines.append(line)
      break
  # copy rest of old lines
  for line in f:
    lines.append(line)
  # delete old line in file
  f.seek(0)
  f.truncate(0)
  # write new lines to file
  f.writelines(lines)