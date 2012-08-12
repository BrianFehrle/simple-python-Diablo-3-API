#!/usr/bin/python
import urllib2
import simplejson as json

def call(url = None, last_modified = None, return_type = "JSON"):
    """
    Function call executes an api call. It accepts three inputs:
    1 the URL, which if null the function will return an error
    2 the last modified date string, which if null, the function will not send to the api call
    3 return_type, which if null will default to JSON, default will just return what the api call returned

    Function Returns
    The function will always return two elements.
    If the function failed, it will return first the return code, second the error message
    If the api call succeded, it will return first the reply from the api call, then the new last modified date
    If the api call replied saying that the address has not been modified, it will return first '1', then 'HTTP Error 304: Not Modified'
    """
    
    if url == None:
        raise NameError("URL is null!")
    if last_modified == "None":
        last_modified = None;
    try:
        # Request the url specified.
        req = urllib2.Request(url)
        if last_modified != None:
            req.add_header("If-Modified-Since", last_modified)
        url_handle = urllib2.urlopen(req)
        headers = url_handle.info()
        new_last_modified = headers.getheader("Last-Modified") 
        url_contents = urllib2.urlopen(req).read()

        # Return JSON type
        if return_type == "JSON":
            #print "DEBUG: Returning a json type" 
            try:
                return json.loads(url_contents), new_last_modified
            except Exception, e:
                print "ERROR: Could not pass string into json parser. [%s]" % e
                raise

        # Return a normal type
        elif return_type.lower() == "default":
            return url_contents, new_last_modified

        # Return type specified unknown
        else:
            raise NameError("Unknown return_type [%s]" % return_type)

    # Catch HTTP Errors (such as not modified)
    except urllib2.HTTPError, e:
        err = str(e.read())
        if str(e) == "HTTP Error 304: Not Modified":
            return e, None
        #print "DEBUG: HTTP ERROR [%s]" % err
        try:
            return json.loads(err), None
        except Exception, e:
            #print "ERROR: Could not pass string into json parser. [%s]" % e
            raise

