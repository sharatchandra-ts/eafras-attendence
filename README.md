# EAFRAS
### Edge-Assisted Face Recognition Attendance System using ESP32-CAM

EAFRAS is a smart attendance system that automates attendance marking using embedded vision and face recognition, with an emphasis on edge processing and local deployment. The system minimizes data transfer by performing face detection and preprocessing on the ESP32-CAM, while delegating face recognition and attendance logic to a local server.

## Problem Statement

Traditional attendance systems are time-consuming and prone to proxy attendance. Existing biometric systems are often expensive, centralized, and lack flexibility. There is a need for a low-cost, embedded, and intelligent attendance system that is secure, automated, and suitable for classroom environments.

## Objectives

- Automate attendance using face recognition

- Perform maximum possible processing locally (edge-assisted)

- Prevent duplicate attendance using session-based cooldown

- Implement basic liveness verification using randomized background challenges

- Maintain accurate date and time–stamped attendance logs
