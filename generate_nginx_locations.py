import os

apache_codes = {100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 421, 422, 423, 424, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511}
return_code = "\t\tlocation = /# {\n\t\t\treturn # \" \";\n\t\t}\n"
proxy_code = "\t\tlocation = /# {\n\t\t\tproxy_pass http://localhost:80/#;\n\t\t}\n"

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
    if i in apache_codes: lines.append(proxy_code.replace("#", str(i).zfill(3)))
    else: lines.append(return_code.replace("#", str(i).zfill(3)))
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