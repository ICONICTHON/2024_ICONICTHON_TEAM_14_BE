package dongguk.havruta.controller;

import dongguk.havruta.dto.UserDto;
import dongguk.havruta.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;

    // 회원가입 페이지 출력 요청 - GetMapping으로 출력 요청 -> PostMapping에서 form에 대한 action 수행
    @GetMapping("/save")
    public String saveForm() {
        return "save";
    }

    @PostMapping("/save")
    public String join(@ModelAttribute UserDto userDto) {
        System.out.println("UserController.save");
        System.out.println("userDTO = " + userDto);
        userService.save(userDto);

        return "index";
    }

}
