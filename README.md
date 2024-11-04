# market-data-dissemination

# Market Data Dissemination Simulator

## Project Overview
The **Market Data Dissemination Simulator** is a distributed asynchronous microservice system designed to provide real-time updates of market data. It consists of a client-server architecture implemented using gRPC. The simulator includes an order book management system that handles multiple instruments and contracts, along with a frontend web application for visualization and management of subscriptions.

## Table of Contents
- [Functional Requirements](#functional-requirements)
  - [Server Component](#server-component)
  - [Client Component](#client-component)
  - [Frontend Web Application](#frontend-web-application)
- [Non-Functional Requirements](#non-functional-requirements)
- [Technical Requirements](#technical-requirements)
- [Milestones & Deliverables](#milestones--deliverables)
- [User Documentation](#user-documentation)

## Functional Requirements

### Server Component
- **Configuration Management**:
  - Read configuration files defining instruments, contracts, and order book depth.
  - Supported formats: JSON or YAML.

- **Order Book Management**:
  - Maintain an order book for multiple instruments.
  - Support operations to add, remove, and update orders.
  - Ensure thread-safe operations for concurrent access.

- **Subscription Management**:
  - Allow clients to subscribe to specific instruments.
  - Provide bidirectional streaming of market data updates.
  - Handle disconnections and re-subscriptions gracefully.

- **Database Integration**:
  - Interface with a database (PostgreSQL or MongoDB) to store:
    - Instrument and contract details
    - Current state of the order book
    - Historical market data for analysis.
  - Implement CRUD operations for data management.

### Client Component
- **User Interface**:
  - Provide a user-friendly interface to manage subscriptions.
  - Display current state of the order book, including bids and asks.

- **Subscription Functionality**:
  - Allow users to subscribe to market data for specific instruments.
  - Display real-time updates received from the server.
  - Support receiving snapshots of the order book on request.

- **Error Handling**:
  - Handle connection errors with appropriate messages.
  - Provide mechanisms for re-connecting and re-subscribing.

### Frontend Web Application
- **Technology Stack**:
  - Built using React.js or Vue.js.
  - Consumes the gRPC API for real-time updates.

- **UI Features**:
  - Dashboard displaying order book and recent trades.
  - Controls for subscribing/unsubscribing to instruments.
  - Visualization of historical data and trends.
  - User authentication for secure access.

## Non-Functional Requirements

- **Performance**: 
  - Server must handle a minimum of 1,000 concurrent connections.
  - Provide updates with latency of less than 100 milliseconds.

- **Scalability**:
  - Support horizontal scaling for increased loads.

- **Reliability**:
  - Ensure data consistency in the order book across clients.
  - Implement recovery mechanisms for failures.

- **Security**:
  - Use secure communication channels (e.g., TLS).
  - Enforce access controls on the database.

## Technical Requirements

- **Programming Languages**:
  - Server: Rust or Golang.
  - Client and Frontend: JavaScript or TypeScript.

- **Database**:
  - PostgreSQL or MongoDB for data storage.
  - Schema design to be defined based on data requirements.

- **Development Environment**:
  - Version control with Git.
  - Containerization with Docker.
  - CI/CD pipeline for automated testing and deployment.

## Milestones & Deliverables
1. **Initial Setup**: Environment configuration and repository creation.
2. **Prototype Development**: Basic server-client communication.
3. **Order Book Implementation**: Complete order book management features.
4. **Client Subscription Features**: Implement user subscription functionalities.
5. **Frontend Development**: Build and integrate the web application.
6. **Testing**: Conduct thorough testing of all components.
7. **Deployment**: Deploy the application to a cloud service.

## User Documentation
- User manual detailing installation, configuration, and usage of the simulator.
- API documentation for gRPC services.
