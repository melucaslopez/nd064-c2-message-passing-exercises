syntax = "proto3";

message OrderMessage {
    enum Status {
        Queued = 0;
        Processing = 1;
        Completed = 2;
        Failed = 3;
    }

    enum Equipment {
        Keyboard = 0;
        Mouse = 1;
        Webcam = 2;
        Monitor = 3;
    }

    string id = 1;
    string created_by = 2;
    Status status = 3 [ default = Queued ];
    string created_at = 4;
    repeated Equipment equipment = 5;
}

Service orderService {
    rpc Create(OrderMessage) returns (OrderMessage)
}