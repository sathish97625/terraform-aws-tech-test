# AWS Terraform Exercise 2

We would like to be able to run the same stack closer to our customers in the US. Please build the same stack in the us-east-1 (Virginia) region. Note that Virginia has a different number of availability zones which we would like to take advantage of for better resilience. As for a CIDR block for the VPC use whatever you feel like, providing it's compliant with RFC-1918 and does not overlap with the dublin network.
 
All the required for are in the folder for the above requirement.
Resiliency has been achieved by autoscaling and launch template, for which configuration has been added.
Connectivity is only from Bastion server.
