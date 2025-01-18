import os
import shlex
import subprocess

def execute_command(command):
    try:
        # Parse the command
        parts = shlex.split(command)

        # Handle IO redirection
        if ">" in parts:
            redir_index = parts.index(">")
            cmd = parts[:redir_index]
            output_file = parts[redir_index + 1]
            with open(output_file, "w") as outfile:
                subprocess.run(cmd, stdout=outfile, stderr=subprocess.STDOUT)
            print(f"Output redirected to {output_file}")
            return
        elif "<" in parts:
            redir_index = parts.index("<")
            cmd = parts[:redir_index]
            input_file = parts[redir_index + 1]
            with open(input_file, "r") as infile:
                subprocess.run(cmd, stdin=infile)
            return

        # Handle piping
        if "|" in parts:
            commands = " ".join(parts).split("|")
            processes = []
            prev_pipe = None

            for cmd in commands:
                cmd_parts = shlex.split(cmd.strip())
                if prev_pipe is None:
                    # First command
                    proc = subprocess.Popen(cmd_parts, stdout=subprocess.PIPE)
                else:
                    # Commands in the middle
                    proc = subprocess.Popen(cmd_parts, stdin=prev_pipe.stdout, stdout=subprocess.PIPE)

                processes.append(proc)
                prev_pipe = proc

            # Capture output of the last process
            output, _ = processes[-1].communicate()
            print(output.decode("utf-8"))
            return

        # Execute a single command
        subprocess.run(parts)

    except FileNotFoundError:
        print("Command not found!")
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    print("Simple Shell: Type 'exit' to quit")
    while True:
        try:
            command = input("shell> ")
            if command.strip().lower() == "exit":
                print("Exiting shell.")
                break
            execute_command(command)
        except KeyboardInterrupt:
            print("\nExiting shell.")
            break

if __name__ == "__main__":
    main()
