from .errors import MymathImageRunFailedException
import docker
import os
import re

class DockerClientHandler:
    def __init__(self):
        add_image_name = os.environ.get('ADD_IMAGE_REPO') or 'myadd'
        add_image_tag = os.environ.get('ADD_IMAGE_TAG') or '1.0'
        self.add_image = '%s:%s' % (add_image_name, add_image_tag)

        sub_image_name = os.environ.get('SUB_IMAGE_REPO') or 'mysub'
        sub_image_tag = os.environ.get('SUB_IMAGE_TAG') or '1.0'
        self.sub_image = '%s:%s' % (sub_image_name, sub_image_tag)

        mul_image_name = os.environ.get('MUL_IMAGE_REPO') or 'mymul'
        mul_image_tag = os.environ.get('MUL_IMAGE_TAG') or '1.0'
        self.mul_image = '%s:%s' % (mul_image_name, mul_image_tag)

        div_image_name = os.environ.get('DIV_IMAGE_REPO') or 'mydiv'
        div_image_tag = os.environ.get('DIV_IMAGE_TAG') or '1.0'
        self.div_image = '%s:%s' % (div_image_name, div_image_tag)

        run_env = os.environ.get('RUN_ENV') or 'local'
        # TODO(AllisonHu64): Add config for development env.
        if run_env == 'local':
            self.client = docker.DockerClient(
                base_url='ssh://ec2-user@ec2-3-92-212-238.compute-1.amazonaws.com',
                use_ssh_client=True)
    
    def run_image(self, image, cmd):
        return self.client.containers.run(image, cmd)

    def run_mymath_add(self, num1, num2):
        result = self.run_image(self.add_image, ['%d' % num1, '%d' % num2]).decode('utf-8')
        return DockerClientHandler.extract_mymath_result(result)

    def run_mymath_sub(self, num1, num2):
        result = self.run_image(self.sub_image, ['%d' % num1, '%d' % num2]).decode('utf-8')
        return DockerClientHandler.extract_mymath_result(result)

    def run_mymath_mul(self, num1, num2):
        result = self.run_image(self.mul_image, ['%d' % num1, '%d' % num2]).decode('utf-8')
        return DockerClientHandler.extract_mymath_result(result)

    def run_mymath_div(self, num1, num2):
        result = self.run_image(self.div_image, ['%d' % num1, '%d' % num2]).decode('utf-8')
        return DockerClientHandler.extract_mymath_result(result)

    def extract_mymath_result(result):
        is_success = re.fullmatch('result: [+-]?\d+\n', result)
        if not is_success:
            raise MymathImageRunFailedException
        else:
            value = int(re.search('[+-]?\d+', result).group(0))
            return value