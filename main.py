from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    client_id, client_secret = "", ""

    i = 4
    wait_time = between(1, 2)

    def on_start(self):
        response = self.client.post("/login", json={"username":"superadmin@swiftdynamics.co.th", "password":'12345678'})
        response_json = response.json()
        token = response_json['token']['token']

        self.headers = {'Authorization': 'Bearer ' + token}

    @task
    def get_company_list(self):
        self.i += 1
        code = f'swd00{self.i}'
        self.client.post("/api/v1/company/", json={"code":code, "title":code})
    
    @task
    def input_device_aot(self):
        self.client.post("/api/v1/devices/input", json={
            "applicationID": "763",
            "applicationName": "CCB-A-FL3_003",
            "deviceName": "CCB-A-FL3_003-PIR1",
            "deviceProfileName": "WINEXT_AN-304C_PIR",
            "deviceProfileID": "9245085f-40b3-432b-bb2e-1862f48f8247",
            "devEUI": "ffffff100003736b",
            "rxInfo": [
                {
                    "gatewayID": "7276ff0045060419",
                    "uplinkID": "fd23b6bd-c036-486b-b991-61347bc702cf",
                    "name": "BKK-G22",
                    "time": "2023-01-17T04:47:19.09478Z",
                    "rssi": -120.0,
                    "loRaSNR": -6.2,
                        "altitude": 0
                    },
                {
                    "gatewayID": "7276ff00450607e2",
                    "uplinkID": "4d5388d8-a94f-4b78-a8ff-e2540fbe4d6d",
                    "name": "BKK-G16",
                    "time": "2023-01-16T22:55:54.82348Z",
                    "rssi": -103.0,
                    "loRaSNR": -0.2,
                    "location": {
                        "latitude": 0,
                        "longitude": 0,
                        "altitude": 0
                    }
                },
                {
                    "gatewayID": "7276ff00450607d0",
                    "uplinkID": "73978620-d206-4e8d-b1ee-ca44b5d04b40",
                    "name": "BKK-G20",
                    "time": "2023-01-17T05:58:05.706589Z",
                    "rssi": -112.0,
                    "loRaSNR": 1.8,
                    "location": {
                        "latitude": 0,
                        "longitude": 0,
                        "altitude": 0
                    }
                },
                {
                    "gatewayID": "7276ff00450607df",
                    "uplinkID": "c0edb79a-cf59-4e69-a975-ca6b428925db",
                    "name": "BKK-G18",
                    "time": "2023-01-17T06:59:23.541419Z",
                    "rssi": -95.0,
                    "loRaSNR": 9,
                    "location": {
                        "latitude": 0,
                        "longitude": 0,
                        "altitude": 0
                    }
                },
                {
                    "gatewayID": "7276ff0045060444",
                    "uplinkID": "b6c91d74-5d51-4d65-af06-fe49804dc93e",
                    "name": "BKK-G50",
                    "time": "2023-01-17T06:59:23.511066Z",
                    "rssi": -104.0,
                    "loRaSNR": -4.8,
                    "location": {
                        "latitude": 0,
                        "longitude": 0,
                        "altitude": 0
                    }
                },
                {
                    "gatewayID": "7276ff00450606ba",
                    "uplinkID": "ae08e317-c504-432b-9525-c6189dd18205",
                    "name": "BKK-G42",
                    "time": "2023-01-17T06:59:11.478273Z",
                    "rssi": -42.0,
                    "loRaSNR": 9.8,
                    "location": {
                        "latitude": 0,
                        "longitude": 0,
                        "altitude": 0
                    }
                }
            ],
            "txInfo": {
                "frequency": 922000000,
                "dr": 5
            },
            "adr": False,
            "fCnt": 21,
            "fPort": 210,
            "data": "AAEEbQEDAAQNwAUAFwF2AAHYgw==",
            "object": {
                "battery": 3.52,
                "trigger_count": 120963
            }
        })