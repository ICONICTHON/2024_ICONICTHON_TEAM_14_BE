package dongguk.havruta.service;

import dongguk.havruta.domain.UserEntity;
import dongguk.havruta.dto.UserDto;
import dongguk.havruta.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    @Autowired
    private final UserRepository userRepository; // jpa, MySQL dependency 추가

    @Autowired
    private final PasswordEncoder passwordEncoder;


    public void save(UserDto userDto) {
        String rawPwd = userDto.getPwd();
        String encodedPwd = passwordEncoder.encode(rawPwd);

        UserEntity userEntity = UserEntity.toUserEntity(userDto);
        userEntity.setPwd(encodedPwd);

        userRepository.save(userEntity);
    }
}