########################
# Function call executes an api call. It accepts three inputs:
# 1 the URL, which if null the function will return an error
# 2 the last modified date string, which if null, the function will not send to the api call
# 3 return_type, which if null will default to JSON, default will just return what the api call returned
########################
# Function Returns
# The function will always return two elements.
# If the function failed, it will return first the return code, second the error message
# If the api call succeded, it will return first the reply from the api call, then the new last modified date
# If the api call replied saying that the address has not been modified, it will return first '1', then 'HTTP Error 304: Not Modified'
########################
