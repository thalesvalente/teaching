import { IsString } from 'class-validator';

export class GetGeminiDataDto {
  @IsString()
  endpoint: string;
}
