def parse_multipart_form_data(handler, body):
    """Function to parse multipart/form-data from the request."""
    try:
        boundary = handler.headers['Content-Type'].split('boundary=')[
            1].encode()
        boundary = b'--' + boundary

        parts = body.split(boundary)
        request_data = {}

        for part in parts:
            if part == b'--\r\n' or part == b'--\n' or part == b'':
                continue  # Skip the last boundary and empty parts

            # Split headers from body
            header, content = part.split(b'\r\n\r\n', 1)
            content = content.rstrip(b'\r\n')  # Remove trailing CRLF

            # Decode headers
            headers = header.decode().split('\r\n')
            content_disposition = [
                h for h in headers if h.startswith('Content-Disposition')]
            if content_disposition:
                disposition = content_disposition[0]
                params = {k.strip(): v.strip('"') for k, v in (param.split('=')
                                                               for param in disposition.split(';') if '=' in param)}
                field_name = params['name']

                # Check if there's a filename parameter
                if 'filename' in params:
                    filename = params['filename']
                    # Store filename and content
                    request_data[field_name] = (filename, content)
                else:
                    # Store field data
                    request_data[field_name] = content.decode('utf-8')

        return request_data
    except Exception as e:
        raise ValueError(f"Failed to parse multipart form data: {str(e)}")
