#!/usr/bin/env python3

from adbc_driver_flightsql import dbapi as flight_sql, DatabaseOptions

# Use an env var in production code!
flight_password = "flight_password"

with flight_sql.connect(uri="grpc+tls://localhost:31337",
                        db_kwargs={"username": "flight_username",
                                   "password": flight_password,
                                   DatabaseOptions.TLS_SKIP_VERIFY.value: "true",
                                   # Not needed if you use a trusted CA-signed TLS cert
                                   }
                        ) as conn:

   with conn.cursor() as cur:
       cur.execute("SELECT n_nationkey, n_name FROM nation WHERE n_nationkey = ?",
                   parameters=[24]
                   )
       x = cur.fetch_arrow_table()
       print(x)


