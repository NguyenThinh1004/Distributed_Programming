import socket

ANSWER = {
    "hello": "Xin chao! Toi la server.",
    "time": "Hien tai toi chua ho tro xem gio. Hay thu cau hoi khac.",
    "name": "Toi la TCP Q&A Server.",
    "help": "Ban co the hoi: hello, name, time, help, bye.",
    "bye": "Tam biet!",
}

def build_answer(question):
    key = question.strip().lower()
    if key in ANSWER:
        return ANSWER[key]
    return "Xin loi, toi chua co cau tra loi cho cau hoi nay."

def start_server():
    host = "0.0.0.0"
    port = 7878

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server dang chay tren {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client da ket noi tu: {addr}")

        try:
            buffer = ""
            ended = False
            while True:
                chunk = client_socket.recv(4096).decode("utf-8")
                if not chunk:
                    break

                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    question = line.strip()
                    if not question:
                        continue

                    if question.lower() == "end":
                        client_socket.sendall("Goodbye!\n".encode("utf-8"))
                        print("Client ket thuc phien lam viec.")
                        ended = True
                        break

                    answer = build_answer(question)
                    client_socket.sendall((answer + "\n").encode("utf-8"))
                    print(f"Da tra loi: {question}")

                if ended:
                    break
        except Exception as e:
            print(f"Co loi xay ra khi xu ly: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
