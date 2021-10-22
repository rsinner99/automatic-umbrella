import io

def is_python_installed(ssh):
    script = 'python --version'
    stdin, stdout, stderr = ssh.exec_command(script)
    error = stderr.read().decode().strip()
    if error:
        return False
    return True

def run_python(ssh, content):
    if not is_python_installed(ssh):
        return {
            'output': None,
            'error': 'Python is not installed. Use Bash script to install Python on remote host.'
        }
    mock_file = io.StringIO.StringIO(content)
    sftp = ssh.open_sftp()
    sftp.putfo(mock_file, '~/script.py')
    sftp.close()

    stdin, stdout, stderr = ssh.exec_command('python ~/script.py')
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    ssh.close()

    result = {
        'output': output,
        'error': error
    }
    return result


def run_bash(ssh, content):
    stdin, stdout, stderr = ssh.exec_command(content)

    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    ssh.close()

    result = {
        'output': output,
        'error': error
    }
    return result