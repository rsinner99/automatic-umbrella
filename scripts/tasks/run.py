import io

def is_python_installed(ssh):
    script = 'python3 --version'
    stdin, stdout, stderr = ssh.exec_command(script, timeout=5)
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

    content = content.replace('"','\\"')
    ssh.exec_command(f'echo "{content}" > ~/script.py')

    stdin, stdout, stderr = ssh.exec_command('python3 ~/script.py', timeout=5)
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    ssh.exec_command('rm ~/script.py')

    ssh.close()
    if error:
        raise OSError(error)
    
    return output


def run_bash(ssh, content):
    stdin, stdout, stderr = ssh.exec_command(content, timeout=5)

    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    ssh.close()
    if error:
        raise OSError(error)

    return output

