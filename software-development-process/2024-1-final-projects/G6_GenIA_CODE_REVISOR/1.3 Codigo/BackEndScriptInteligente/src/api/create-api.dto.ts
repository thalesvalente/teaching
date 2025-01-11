import { IsString, IsNotEmpty } from 'class-validator';

export class CreateApiDto {
  @IsString()
  @IsNotEmpty()
  name: string;

  @IsString()
  @IsNotEmpty()
  url: string;
}
