enable_test = {
	"echo_hi.yaml":False,
	"python_webscrape.yaml":True,
	"python_webscrape_no_setup-python.yaml":True,
}
output_folder = r".github/workflows/"

import os

file_name = "echo_hi.yaml"
check_out_versions = [0,1,2,3,4]
runners = ["ubuntu_latest", "ubuntu-20.04", "ubuntu-18.04"]
with open(file_name) as f:
	template = f.read()
for check_out_version in check_out_versions:
	for runner in runners:
		formatted_template = template.format(runner=runner, check_out_version=check_out_version)
		output_file = output_folder+file_name.replace(".yaml",f"_{runner}_checkout-v{check_out_version}.yaml")
		with open(output_file,'w') as f:
			f.write(formatted_template)
		if not enable_test[file_name]:
			os.remove(output_file)


file_name = "python_webscrape.yaml"
python_setup_versions = [1,2,3,4]
runners = ["ubuntu-20.04", "ubuntu-18.04"]
python_versions = ["3.6","3.7","3.8","3.9","3.10","3.11","3.12","pypy3.6","pypy3.7","pypy3.8","pypy3.9","pypy3.10"]
architectures = ["x64","x86"]
with open(file_name) as f:
	template = f.read()
for architecture in architectures:
	for python_version in python_versions:
		for python_setup_version in python_setup_versions:
			for runner in runners:
				formatted_template = template.format(runner=runner, architecture=architecture,python_version=python_version,python_setup_version=python_setup_version)
				with open(output_folder+file_name.replace(".yaml",f"_{runner}_python-setupv{python_setup_version}_python_{python_version}_{architecture}.yaml"),'w') as f:
					f.write(formatted_template)
				if not enable_test[file_name]:
					os.remove(output_file)

file_name = "python_webscrape_no_setup-python.yaml"
with open(file_name) as f:
	template = f.read()
with open(output_folder+file_name,'w') as f:
	f.write(formatted_template)
if not enable_test[file_name]:
	os.remove(output_file)
