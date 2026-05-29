import socket

def start_client():
    host = "192.168.43.190"
    port = 7878

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print('Da ket noi server. Nhap cau hoi ("End" de ket thuc).')

        while True:
            question = input("Ban hoi: ").strip()
            if not question:
                continue

            client_socket.sendall((question + "\n").encode("utf-8"))
            response = client_socket.recv(4096).decode("utf-8").strip()
            print(f"Server tra loi: {response}")

            if question.lower() == "end":
                break
    except Exception as e:
        print(f"Loi ket noi: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()