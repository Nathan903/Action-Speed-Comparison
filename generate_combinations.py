file_name = "echo_hi.yaml"
output_folder = r".github/workflows/"
check_out_versions = [0,1,2,3,4]
runners = ["ubuntu_latest", "ubuntu-20.04", "ubuntu-18.04"]
with open(file_name) as f:
	template = f.read()
for check_out_version in check_out_versions:
	for runner in runners:
		formatted_template = template.format(runner=runner, check_out_version=check_out_version)
		with open(output_folder+file_name.replace(".yaml",f"_{runner}_checkout-v{check_out_version}.yaml"),'w') as f:
			f.write(formatted_template)