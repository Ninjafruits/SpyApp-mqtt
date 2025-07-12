#!/usr/bin/env python3
import time
import argparse
import paho.mqtt.client as mqtt

# Default parameters
BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'test'
TOTAL  = 1_000_000

def on_connect(client, userdata, flags, reasonCode, properties):
    print(f"[Connected] reason={reasonCode}")

def on_publish(client, userdata, mid):
    # Called when a message that was to be sent using the publish() call has completed transmission to the broker.
    pass

def main(broker, port, topic, total):
    # 1) Create client & tune buffering
    client = mqtt.Client(protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Increase how many QoS 0 messages can be “in flight” before blocking
    client.max_inflight_messages_set(10_000)
    # Allow unlimited queuing of outgoing messages
    client.max_queued_messages_set(0)

    # 2) Connect & start the network loop in a background thread
    client.connect(broker, port)
    client.loop_start()

    # 3) Blast out messages with no sleep
    print(f"Publishing {total} messages to {broker}:{port} → topic '{topic}'")
    start = time.time()
    for i in range(total):
        payload = f"msg-{i}"
        rc = client.publish(topic, payload, qos=0).rc
        if rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"[!!] publish {i} failed, rc={rc}")
            break

    end = time.time()
    sent = i+1
    duration = end - start
    print(f"Published {sent} messages in {duration:.2f}s → {sent/duration:.0f} msg/s")

    # 4) Graceful teardown
    time.sleep(1)   # give lib a moment to flush
    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="High-speed MQTT publisher")
    parser.add_argument('--broker', '-b', default=BROKER, help="MQTT broker address")
    parser.add_argument('--port',   '-p', type=int, default=PORT, help="MQTT broker port")
    parser.add_argument('--topic',  '-t', default=TOPIC, help="MQTT topic to publish to")
    parser.add_argument('--total',  '-n', type=int, default=TOTAL, help="Number of messages to send")
    args = parser.parse_args()

    main(args.broker, args.port, args.topic, args.total)
