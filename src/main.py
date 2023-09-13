from conf.settings import settings

def main():
    source_stream_port = settings.get('input_stream')
    chosen_input_stream = settings.get(source_stream_port)

    input_stream = chosen_input_stream.create_stream_port()
    print(input_stream)

if __name__ == "__main__":
    main()