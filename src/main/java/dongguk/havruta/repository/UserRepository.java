package dongguk.havruta.repository;

import dongguk.havruta.domain.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository // <객체 type, pk type>
public interface UserRepository extends JpaRepository<UserEntity, String> {

}
