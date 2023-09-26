import requests

def get_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"

    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    data = {
        "app_id": "cli_a1fa75a4dabcd00b",
        "app_secret": "0p27zWpHCetvHgEeg5LYpedUjZkokUQy"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_data = response.json()
        tenant_access_token = json_data.get("tenant_access_token")
        if tenant_access_token:
            print("tenant_access_token:", tenant_access_token)
            return tenant_access_token
        else:
            print("Failed to get tenant_access_token from response data.")
            return -1
    else:
        print("Failed to make request. Status code:", response.status_code)
        return -1
