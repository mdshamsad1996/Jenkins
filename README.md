### Jenkins with integration of Docker file

 configure jenkisn in Ec2
 
    sudo yum remove java-1.7.0-openjdk
    sudo yum install java-1.8.0
      
 Download and Install Jenkins
  
      sudo yum update –y
      sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
      sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
      sudo yum install jenkins -y
      sudo service jenkins start
      sudo systemctl start jenkins.service
      sudo systemctl enable jenkins.service
      
  Install git in Ec2
    
      sudo yum install git
  
Configure Docker in Ec2

    sudo yum update -y
    sudo yum install docker
    sudo service docker start
    sudo usermod -aG docker ${USER}
    
To run Dockerfile in Jenkins (fix permission issue)

    sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
    sudo chmod g+rwx "$HOME/.docker" -R

Please make sure to install Docker pipeline plugin in Jenkins

References:

    https://medium.com/@mohan08p/install-and-configure-jenkins-on-amazon-ami-8617f0816444
 
   http://mirrors.jenkins-ci.org/redhat/
 
   https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket




  
