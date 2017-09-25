from client import RoutesClient

def main():
    routes_client = RoutesClient(
        base_url='http://192.168.99.100:8080', 
        key_path='private.key',
        client_id=1
    )
    print(routes_client.get_routes())

if __name__ == '__main__':
    main()
