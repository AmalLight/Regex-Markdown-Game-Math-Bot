# Doc about Rclone

---

1. ## Why we do that ?

    Debug MIC ( or MC ),
    the client for Minio. it doesn't work well.

    Mc is able to copy set X 's content into set Y,
    but it fails for all if all files are not processed.

    So for this reason we are suggesting to use:

    - bash iteration ( for el in Set ; do .. done )
      for each files contained into set X .
      But mc doesn’t keep good connection with load balancer,
      for this some files fall.

    - rclone package.


2. ## rclone Proprety

    + preserve integrity.

    + copy more files using parallelism technique.

    + skip files already copied before.

3. ## Sources

    - official page for get it and downloading:
      <https://rclone.org>
---

1. ## Steps


    1. ### [install](#install) the software
    2. ### [config](#config) two different instances
    3. ### [execute](#execute) the correct commands for clone
    ---

## Install the software {#install}

* `bash apt get install rclone -y`

## Config two different instances {#config}

1. init with : `rclone config`
2. save this on /home/{Your_User}/.config/rclone/rclone.conf

        [minio1]
        type = ***
        env_auth = ***
        access_key_id = ***
        secret_access_key = ***
        region =
        endpoint = ***
        location_constraint = ***
        server_side_encryption = ***

        [minio2]
        type = ***
        env_auth = ***
        access_key_id = ***
        secret_access_key = ***
        region =
        endpoint = ***
        location_constraint = ***
        server_side_encryption = ***

## Execute the correct commands for clone {#execute}


### Rule:
    - rclone copy --progress --checksum \
      minio1:bucket1/sub_folder1/.../point1 \
      minio2:bucket2/sub_folder2/.../point2

### True Copmmand
    - rclone copy --progress --checksum \
      minio1:semantic-scholar/dump/filtered/s2-corpus-xxx.json \
      minio2:semantic-scholar/dump/filtered/s2-corpus-xxx.json
