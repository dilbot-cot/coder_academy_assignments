let notificationPermissions = Notification.permission;

console.log(`Notification status is ${notificationPermissions}`);

switch (notificationPermissions){
    case "default":
        console.log("User has not been asked about notifications yet");
        askNotificationPermission();
        break;
    case "granted":
        console.log("User has granted notifications");
        setTimeout(() => {
            console.log("Hey Hey")
            new Notification("Example notification",{
                body: "hey hey"
            })
        }, 5000);
        break;
    case "denied":
        console.log("User has rejected notifications");
        break;
    default:
        console.log("No notifications, this is an error");
        break;
}


function askNotificationPermission(){
    Notification.requestPermission().then((status) => {
        console.log(status);
        notificationPermissions = status;
      });
}