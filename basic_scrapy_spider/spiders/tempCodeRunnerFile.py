def auth():
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

        credentials = None

        try:
            credentials = service_account.Credentials.from_service_account_file(
                'google_auth_key.json',
                scopes=scope
            )
        except exceptions.DefaultCredentialsError:
            print("Failed to get credentials.")