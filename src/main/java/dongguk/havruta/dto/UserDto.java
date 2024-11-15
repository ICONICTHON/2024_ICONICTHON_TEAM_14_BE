package dongguk.havruta.dto;
import dongguk.havruta.domain.UserEntity;
import lombok.*;


@Getter
@Setter
@NoArgsConstructor
@ToString
public class UserDto {
    private String userID;
    private String pwd;
    private String userName;
    private String userEmail;

    public static UserDto toUserDtO(UserEntity userEntity) {
        UserDto userDto = new UserDto();

        userDto.setUserID(userEntity.getUserID());
        userDto.setPwd(userEntity.getPwd());
        userDto.setUserName(userEntity.getUserName());
        userDto.setUserEmail(userEntity.getUserEmail());

        return userDto;
    }
}