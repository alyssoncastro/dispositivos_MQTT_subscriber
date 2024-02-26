
import unittest
import paho.mqtt.client as mqtt
import json
import threading
import time



#RECEBIMENTO
class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.qos_level = 0



    def test_recebimento(self):

        #inicializa o subscriber
        self.received_message = None
        subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "test_subscriber")
        subscriber.on_message = self.on_message
        subscriber.connect("localhost", 1883, 60)
        subscriber.subscribe("sensor/gases", qos=self.qos_level)


        #puublicando no tópico
        simulated_message = '{"sensor": {"name": "Test Sensor"}, "reading": {"CO": 50.0}}'
        publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "test_publisher")

        publisher.connect("localhost", 1883, 60)
        publisher.publish("sensor/gases", simulated_message, qos=self.qos_level)


        tempo = time.time()

        while self.received_message is None and time.time() - tempo < 5:
            subscriber.loop_start()
            time.sleep(0.1)

        #verifiacando
        self.assertIsNotNone(self.received_message)


    def on_message(self, client, userdata, message):
        self.received_message = message.payload.decode()



if __name__ == '__main__':
    unittest.main()
