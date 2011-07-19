'''Functions that load and write PEM-encoded files.'''

import base64

def load_pem(contents, pem_start, pem_end):
    '''Loads a PEM file.

    Only considers the information between lines "pem_start" and "pem_end". For
    private keys these are  '-----BEGIN RSA PRIVATE KEY-----' and 
    '-----END RSA PRIVATE KEY-----'

    @param contents: the contents of the file to interpret
    @param pem_start: the start marker of the PEM content, such as
        '-----BEGIN RSA PRIVATE KEY-----'
    @param pem_end: the end marker of the PEM content, such as
        '-----END RSA PRIVATE KEY-----'

    @return the base64-decoded content between the start and end markers.

    @raise ValueError: when the content is invalid, for example when the start
        marker cannot be found.

    '''

    pem_lines = []
    in_pem_part = False

    for line in contents.split('\n'):
        line = line.strip()

        # Handle start marker
        if line == pem_start:
            if in_pem_part:
                raise ValueError('Seen start marker "%s" twice' % pem_start)

            in_pem_part = True
            continue

        # Skip stuff before first marker
        if not in_pem_part:
            continue

        # Handle end marker
        if in_pem_part and line == pem_end:
            in_pem_part = False
            break

        pem_lines.append(line)

    # Do some sanity checks
    if not pem_lines:
        raise ValueError('No PEM start marker "%s" found' % pem_start)

    if in_pem_part:
        raise ValueError('No PEM end marker "%s" found' % pem_end)

    # Base64-decode the contents
    pem = ''.join(pem_lines)
    return base64.decodestring(pem)

def save_pem(contents, pem_start, pem_end):
    '''Saves a PEM file.

    The PEM file will start with the 'pem_start' marker, then the
    base64-encoded content, and end with the 'pem_end' marker.

    @param contents: the contents to encode in PEM format
    @param pem_start: the start marker of the PEM content, such as
        '-----BEGIN RSA PRIVATE KEY-----'
    @param pem_end: the end marker of the PEM content, such as
        '-----END RSA PRIVATE KEY-----'

    @return the base64-encoded content between the start and end markers.

    '''

    b64 = base64.encodestring(contents).strip()
    pem_lines = [pem_start]
    
    for block_start in range(0, len(b64), 64):
        block = b64[block_start:block_start + 64]
        pem_lines.append(block)

    pem_lines.append(pem_end)
    pem_lines.append('')

    return '\n'.join(pem_lines)
    