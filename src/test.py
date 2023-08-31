import urllib.request
import json

        my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ3MmE1ZDEzLTM0MGMtNGQ1NS1hZjFkLTVlZjg5MTc4NzViYiIsImlhdCI6MTU3MzUyNjU5Niwic3ViIjoiZGV2ZWxvcGVyL2JmZmI5YWI5LTY5MzUtYWQ2Zi1iNzMyLTU0ODg1ZWNjMWMzZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDIuNy4yMDYuODQiXSwidHlwZSI6ImNsaWVudCJ9XX0.S5kRVmml4P_9r6E1Cp-0XH6Gl01gf2KhXAbx3HODVQQRuKyyUx6VTyweHPyFlvp7Ovlv0VgEEGE994AM2tZ49w"
        my_key = my_key.rstrip("\n")
        base_url = "https://api.clashroyale.com/v1"

        endpoint = "/cards"

              request = urllib.request.Request(
                        base_url+endpoint,
                 None,
                        {
           "Authorization": "Bearer %s" % my_key
                        }
                )
        response = urllib.request.urlopen(request).read().decode("utf-8")

        print(response)
        