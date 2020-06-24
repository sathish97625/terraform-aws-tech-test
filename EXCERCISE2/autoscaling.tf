resource "aws_launch_template" "sample" {
  name_prefix                 = "launch-templatete-nginx"
  image_id                    = "ami-cdbfa4ab"
  instance_type               = "t2.small"
  tags                        = {
    Owner     = "SathishMamidala"
    Project   = "Tech Test"
  }
}

resource "aws_autoscaling_group" "sample" {
  availability_zones = ["${var.region}a"]
  desired_capacity   = 1
  max_size           = 1
  min_size           = 1

  launch_template {
  id      =  aws_launch_template.sample.id
  version = "$Latest"
  }

}
