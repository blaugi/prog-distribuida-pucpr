import etcd3
import time
import sys

def main():
    try:
        client = etcd3.client()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    coordination_key = 'status'
    
    print("Aguardando")
    
    client.watch_once(coordination_key)

    for i in range(1, 11):
        print(i)
        time.sleep(1)
        
    print("Fim")

if __name__ == "__main__":
    main()


