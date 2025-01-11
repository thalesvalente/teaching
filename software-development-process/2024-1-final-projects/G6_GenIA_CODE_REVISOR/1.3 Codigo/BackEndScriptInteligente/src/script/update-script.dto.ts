import { IsString, IsNotEmpty } from 'class-validator';

export class UpdateScriptDto {
  @IsString()
  @IsNotEmpty()
  content: string;
}
