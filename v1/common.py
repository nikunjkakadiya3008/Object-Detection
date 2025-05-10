from fastapi.responses import JSONResponse

def success_response(status_code, message, data={}):
    return JSONResponse(
        status_code=status_code,
        content={'message': message, 'data':data}
    )

def error_response(status_code, message, data={}):
    return JSONResponse(
        status_code=status_code,
        content={'message': message, 'data':data}
    )

