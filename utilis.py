import hashlib
def generate_id(text):

    return hashlib.md5(text.encode()).hexdigest()

def prepare_payload(text):
    return {"text":text}

