package dongguk.havruta.domain;

import dongguk.havruta.dto.UserDto;
import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.security.crypto.password.PasswordEncoder;

@Entity
@Getter @Setter
@NoArgsConstructor
@Table(name = "user")
public class UserEntity {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id // primary key
    private String userID;

    @Column(length = 100)
    private String pwd;

    @Column(length = 100)
    private String userName;

    @Column(length = 100)
    private String userEmail;

    @Builder
    public static UserEntity toUserEntity(UserDto userDto) {
        UserEntity userEntity = new UserEntity();

        userEntity.userID = userDto.getUserID();
        userEntity.pwd = userDto.getPwd();
        userEntity.userName = userDto.getUserName();
        userEntity.userEmail = userDto.getUserEmail();

        return userEntity;
    }
}
