![den9](https://github.com/user-attachments/assets/12a6491d-ecb5-4d4e-b605-9c1598e78b75)

The repository includes the complete pipeline of DDoS detection with data generation

1. Simulating the DDoS attack (`traffic_creator`): We have python scripts that create and orchestrate a completely random scenario of DDoS attack over a Software-Defined Network using mininet library of python.
2. Capturing the data (`packet_capturer`) : Uses tcp dump to capture traffic data and dump it into file
3. Preprocessing (`preprocessing_data`) : Preprocessing the traffic data to filter relevant fields and create valuable attributes from it using awk and python.
4. ML algorigthm (`jupyter_notebook`) : It contains the ML model that was trained and tested with data.
